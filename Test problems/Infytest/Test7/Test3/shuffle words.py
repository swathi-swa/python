def generate_sentences(subjects,verbs,objects):
    sen=[]
    for i in subjects:
        for j in verbs:
            for k in objects:
                sen.append(i+" "+j+" "+k)
    return sen

subjects=list(input().split())
verbs=list(input().split())
objects=list(input().split())
s=generate_sentences(subjects,verbs,objects)
for i in s:
    print(i)
