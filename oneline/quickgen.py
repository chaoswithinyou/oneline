from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class quickgen:
    def __init__(self, model_name):
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)

    def predict(self, texts, max_input_length=1024, max_gen_length=256):
        input_tensors = self.tokenizer(
            texts,
            max_length=max_input_length,
            padding=True,
            truncation=True,
            return_tensors="pt",
        ).to(self.device)
        if self.device != "cpu":
            with torch.inference_mode(), torch.autocast(
                dtype=torch.float16, cache_enabled=True, device_type="cuda"
            ):
                outputs = self.model.generate(
                    input_ids=input_tensors["input_ids"],
                    attention_mask=input_tensors["attention_mask"],
                    max_length=max_gen_length,
                    min_length=0,
                )
        else:
            outputs = self.model.generate(
                input_ids=input_tensors["input_ids"],
                attention_mask=input_tensors["attention_mask"],
                max_length=max_gen_length,
                min_length=0,
            )
        return [
            self.tokenizer.decode(
                output, skip_special_tokens=True, clean_up_tokenization_spaces=True
            )
            for output in outputs
        ]
