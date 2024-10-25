s = "AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design."
word = 1
for i in range (len(s)):
    if s[i]==' ':
        word += 1
print("Word count: ",word)
total_words=0
for i in range (26):
    word_count=0;cap_letter=chr(i+65);small_letter=chr(i+97)
    if s[0]==cap_letter or s[0]==small_letter:
        word_count += 1
    for j in range (len(s)):
        if s[j]==' ':
            if s[j+1]==cap_letter or s[j+1]==small_letter:
                word_count += 1
    total_words += word_count
    print(f"Word started form {cap_letter} are: {word_count}")
print(f"Total words count by adding word count of individual alphabet: {total_words}")
