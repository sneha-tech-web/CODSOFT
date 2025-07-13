import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
from torch import nn
import numpy as np

# ===============================
# Pre-trained CNN Encoder (ResNet)
# ===============================
class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        for param in resnet.parameters():
            param.requires_grad = False  # Freeze ResNet

        self.resnet = nn.Sequential(*list(resnet.children())[:-1])  # Remove last FC
        self.linear = nn.Linear(resnet.fc.in_features, embed_size)
        self.bn = nn.BatchNorm1d(embed_size)

    def forward(self, images):
        features = self.resnet(images)
        features = features.reshape(features.size(0), -1)
        return self.bn(self.linear(features))


# ===============================
# Decoder RNN (LSTM)
# ===============================
class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=1):
        super(DecoderRNN, self).__init__()
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_size, vocab_size)

    def forward(self, features, captions):
        embeddings = self.embed(captions[:, :-1])
        inputs = torch.cat((features.unsqueeze(1), embeddings), 1)
        hiddens, _ = self.lstm(inputs)
        outputs = self.linear(hiddens)
        return outputs

    def sample(self, features, states=None, max_len=20):
        "Generate caption from image features"
        sampled_ids = []
        inputs = features.unsqueeze(1)
        for _ in range(max_len):
            hiddens, states = self.lstm(inputs, states)  # (batch_size, 1, hidden_size)
            outputs = self.linear(hiddens.squeeze(1))     # (batch_size, vocab_size)
            _, predicted = outputs.max(1)
            sampled_ids.append(predicted.item())
            inputs = self.embed(predicted).unsqueeze(1)
        return sampled_ids

# ===============================
# Dummy Tokenizer for Testing
# ===============================
class DummyTokenizer:
    def __init__(self):
        self.word2idx = {"<start>": 1, "<end>": 2, "a": 3, "dog": 4, "on": 5, "grass": 6}
        self.idx2word = {idx: word for word, idx in self.word2idx.items()}
        self.vocab_size = len(self.word2idx) + 1

# ===============================
# Image Preprocessing
# ===============================
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(image_path).convert('RGB')
    return transform(image).unsqueeze(0)

# ===============================
# Caption Generation
# ===============================
def generate_caption(image_path, encoder, decoder, tokenizer):
    image_tensor = preprocess_image(image_path)
    features = encoder(image_tensor)
    sampled_ids = decoder.sample(features)
    caption = [tokenizer.idx2word.get(idx, '') for idx in sampled_ids]
    return ' '.join(caption)

# ===============================
# Main Execution
# ===============================
if __name__ == "__main__":
    # Load models
    embed_size = 256
    hidden_size = 512
    tokenizer = DummyTokenizer()

    encoder = EncoderCNN(embed_size)
    decoder = DecoderRNN(embed_size, hidden_size, tokenizer.vocab_size)

    # Load an example image
    image_path = "example.jpg"  # Make sure this image exists

    # Generate and print caption
    caption = generate_caption(image_path, encoder, decoder, tokenizer)
    print("Generated Caption:", caption)