import torch
import streamlit as st
from transformers import MobileBertTokenizer, MobileBertForSequenceClassification

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = MobileBertTokenizer.from_pretrained('./xlnet_model')
model = MobileBertForSequenceClassification.from_pretrained('./xlnet_model')
model.to(device)
model.eval()