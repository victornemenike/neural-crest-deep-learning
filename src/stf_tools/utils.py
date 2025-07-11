import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from captum.attr import InputXGradient, IntegratedGradients, Saliency
from grelu.sequence.format import convert_input_type
from typing import Callable, List, Optional, Union

def quantile_normalize(df):
    sorted_df = np.sort(df.values, axis=0)
    mean_sorted = np.mean(sorted_df, axis=1)
    ranks = np.argsort(np.argsort(df.values, axis=0), axis=0)
    normalized = mean_sorted[ranks]
    return pd.DataFrame(normalized, columns=df.columns, index=df.index)




def get_captum_integrated_gradients(
        model,
        seqs: Union[pd.DataFrame, np.array, List[str]],
        genome: Optional[str] = None,
        prediction_transform: Optional[Callable] = None,
        device: Union[str, int] = "cpu",
        correct_grad: bool = False,
        multiply_by_inputs: bool = True,
        **kwargs,
    ) -> np.array:

    r"""
        Args:

            forward_func (Callable): The forward function of the model or any
                    modification of it
            multiply_by_inputs (bool, optional): Indicates whether to factor
                    model inputs' multiplier in the final attribution scores.
                    In the literature this is also known as local vs global
                    attribution. If inputs' multiplier isn't factored in,
                    then that type of attribution method is also called local
                    attribution. If it is, then that type of attribution
                    method is called global.
                    More detailed can be found here:
                    https://arxiv.org/abs/1711.06104

                    In case of integrated gradients, if `multiply_by_inputs`
                    is set to True, final sensitivity scores are being multiplied by
                    (inputs - baselines).
        """

    # One-hot encode the input
    seqs = convert_input_type(seqs, "one_hot", genome=genome, add_batch_axis=True)

    # Add transform to model
    model.add_transform(prediction_transform)
    model = model.eval()

    # Empty list for the output
    attributions = []

    attributer = IntegratedGradients(model.to(device), multiply_by_inputs=multiply_by_inputs)

    # Calculate attributions for each sequence
    with torch.no_grad():
        for i in range(len(seqs)):
            X_ = seqs[i : i + 1].to(device)  # 1, 4, L
            attr = attributer.attribute(X_)
            attributions.append(attr.cpu().numpy())

    attributions = np.vstack(attributions)

    # Correct gradients
    if correct_grad:
        attributions -= attributions.mean(1, keepdims=True)

    return attributions