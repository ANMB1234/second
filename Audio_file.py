from pathlib import Path




s

class AudioFile:
    
    ext:str
    
    def __init__(self,filepath:Path)->None:
        if not filepath.suffix==self.ext:
            raise ValueError("invalid file format")
        self.filepath=filepath







class MP3File(AudioFile):
    ext = ".mp3"
    
    def play(self)->None:
        print(f"playing {self.filepath} as mp3")






class WavFile(AudioFile):
    ext=".wav"
    def play(self) -> None:
        print(f"playin {self.filepath} as wav")






class OggFile(AudioFile):
    ext=".ogg"
    
    def play(self)->None:
        print(f"playing {self.filepath} as ogg")