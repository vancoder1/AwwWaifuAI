import torch
import torchaudio
from playsound import playsound

class TTS:
    def __init__(self):
        self.language = 'en'
        self.model_id = 'v3_en'
        self.speaker = 'en_107'
        self.sample_rate = 48000
        self.device = torch.device('cpu')
    
    def process_audio(self, input_text):
        model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=self.language,
                                     speaker=self.model_id)
        model.to(self.device)  # gpu or cpu
        audio = model.apply_tts(text=input_text,
                        speaker=self.speaker,
                        sample_rate=self.sample_rate)
        torchaudio.save('cache\\ai_response_tts.mp3',
                  audio.unsqueeze(0),
                  sample_rate=self.sample_rate)