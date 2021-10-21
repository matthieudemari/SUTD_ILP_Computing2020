def convert_seconds(total_seconds):
    seconds = total_seconds
    minutes = total_seconds/60
    hours = minutes/60
    return seconds, minutes, hours

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))

Answers:
(7, 0.11666666666666667, 0.0019444444444444444)
(67, 1.1166666666666667, 0.018611111111111113)
(1024, 17.066666666666666, 0.28444444444444444)