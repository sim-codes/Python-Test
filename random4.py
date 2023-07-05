from random import choices

generated_num = choices("01", k=4)
generated_num = "".join(generated_num)

print(generated_num)
