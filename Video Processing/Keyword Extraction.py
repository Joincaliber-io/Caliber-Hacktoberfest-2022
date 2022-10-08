#pip install transformers==4.11.3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import librosa
import transformers
import pandas as pd
import torch
from operator import itemgetter

audio, rate = librosa.load("Generated\Audio\Audio_1.wav", sr = 16000)


tokenizer = transformers.Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = transformers.Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

input_values = tokenizer(audio, return_tensors = "pt").input_values
# Storing logits (non-normalized prediction values)
logits = model(input_values).logits

# Storing predicted ids
prediction = torch.argmax(logits, dim = -1)

# Passing the prediction to the tokenzer decode to get the transcription
transcription = tokenizer.batch_decode(prediction)[0]

# Printing the transcription
#print(transcription)

Key = transcription.lower()
print(Key)  



