import config
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader


def FineTune():
    model = SentenceTransformer(config.MODEL_PATH)

    train_examples = [
        InputExample(texts=["razer game mouse", "automatic data processing machines"], label=0.95),
        InputExample(texts=["razer game mouse", "gaming machines"], label=0.1),
    ]

    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)

    train_loss = losses.CosineSimilarityLoss(model=model)

    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=1000,
        warmup_steps=100,
        output_path=config.FINETUNED_MODEL_PATH
    )


if __name__ == "__main__":
    FineTune()