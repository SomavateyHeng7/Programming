sentence = input('Write a sentence:')
length = int(len(sentence))
mid = length /2 
if mid % 2 == 0:
    firsthalf = sentence[:int(mid)]
    secondhalf = sentence[int(mid):int(length)]
else:
    firsthalf = sentence[:int(mid+1)]
    secondhalf = sentence[int(mid+1):int(length)]
print(f'First half: {firsthalf}')
print(f'Second half: {secondhalf}')