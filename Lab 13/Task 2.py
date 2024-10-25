s = "AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design."
total_alphabets=0
for i in range (26):
    letter_count=0;cap_letter=chr(i+65);small_letter=chr(i+97)
    for j in range (len(s)):
        if s[j]==cap_letter or s[j]==small_letter:
            letter_count += 1
    total_alphabets += letter_count
    print(f"Letter {cap_letter} appears {letter_count} times")
print(f"Total alphabets in teh paragraph: {total_alphabets}")
print(f"Total characters in teh paragraph: {len(s)}")
