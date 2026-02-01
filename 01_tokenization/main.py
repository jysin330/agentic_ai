import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, world!"
token = enc.encode(text)
print(token)

decoded_text = enc.decode(token)
print(decoded_text)
decoded_text = enc.decode([13225, 11, 2375, 0])

print(decoded_text)