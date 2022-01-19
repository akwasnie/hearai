from typing import Tuple
import numpy as np
import torch
import torch.nn as nn

from torch.optim import Adam

from models.transformers.pretrained_transformer import HubertTransformer


def generate_mockup_input(
    batch_size: int, input_shape: Tuple, value_range: Tuple
) -> torch.Tensor:
    """
    Function creates PyTorch tensor of specified shape with values in provided range.
    Args:
        batch_size (int): Number of instances in a single batch.
        input_shape (Tuple): Shape of input for single data instance.
        value_range (Tuple): Range of value to generate random float values from.

    Returns:
        (torch.Tensor) Mockup data tensor.
    """
    return torch.Tensor(
        np.random.uniform(
            low=value_range[0], high=value_range[1], size=(batch_size,) + input_shape
        )
    )


def generate_mockup_output(batch_size: int, num_classes: int) -> torch.Tensor:
    """
    Function creates PyTorch tensor which imitates output for a classifier model.

    Args:
        batch_size (int): Number of instances in a batch.
        num_classes (int): Number of classes to predict.

    Returns:
        (torch.Tensor) Mockup classification output.
    """
    classes = np.random.randint(low=0, high=num_classes, size=batch_size)
    classes_one_hot = np.zeros((batch_size, num_classes))
    classes_one_hot[np.arange(batch_size), classes] = 1

    return torch.Tensor(classes_one_hot)


if __name__ == '__main__':
    batch_size = 4
    input_shape = (7, 512,)
    value_range = (0., 1.)
    num_classes = 10240

    feature_extractor_output = generate_mockup_input(
        batch_size=batch_size, input_shape=input_shape, value_range=value_range
    )
    labels = generate_mockup_output(batch_size=batch_size, num_classes=num_classes)

    # simulate model training
    checkpoint = 'facebook/hubert-large-ls960-ft'
    model = HubertTransformer(checkpoint=checkpoint, output_features=34)
    loss_fn = nn.functional.cross_entropy
    optimizer = Adam(model.parameters(), lr=1e-4)
    epochs = 10

    epoch = 0
    for epoch in range(epochs):
        X, y_true = feature_extractor_output, labels

        y_pred = model(X)
        loss = loss_fn(y_pred, y_true)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        if (epoch % 10) == 0:
            print(f'Epoch {epoch}/{epochs}, loss: {loss}')

    print(f"Predicted labels: {np.argmax(model(X).detach().numpy(), axis=1)}")
    print(f"True labels: {np.argmax(y_true, axis=1)}")
