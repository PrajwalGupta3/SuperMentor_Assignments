#Assignment Name : Text Challenges
#Description :Collect 20 messy sentences and identify slang, emojis, typos; explain preprocessing needed.




# Assignment (20/03/2026)
# Assignment Name : Text Challenges

# Description:
# Collect 20 messy sentences and identify slang, emojis, typos,
# and explain preprocessing needed.

# Messy Sentences:
# 1. OMG!!! this movie is sooo goooood 😍🔥
# 2. u coming 2 class??
# 3. I cant beleive this happend!!!
# 4. LOL that was funny 😂😂
# 5. plzz send me d notes asap!!!
# 6. This is gr8!!!
# 7. heyyy what r u doing???
# 8. I luv this song sooo much!!!
# 9. wtf was that 😡
# 10. gud mrng!! hv a nice day 😊
# 11. Noooooo!!!!!
# 12. okkkkk I'll do it later
# 13. y r u late???
# 14. that was awsm brooo
# 15. idk what to say...
# 16. brb in 5 mins
# 17. thnx alot!!!
# 18. dis is not gud
# 19. c u soon!!
# 20. I m sooo tired 😴

# Issues Identified:

# 1. Slang Words:
# omg, lol, wtf, brb, idk

# 2. Short Forms:
# u (you), r (are), d (the), m (am), c (see), hv (have)

# 3. Emojis:
# 😍🔥😂😡😊😴

# 4. Typos:
# beleive (believe), happend (happened), gud (good), awsm (awesome)

# 5. Repeated Characters:
# sooo, goooood, heyyy, okkkkk, brooo

# 6. Punctuation Noise:
# !!!, ???, ...

# 7. Case Issues:
# OMG (uppercase), inconsistent capitalization

# Preprocessing Steps Required:

# 1. Convert text to lowercase
# 2. Remove punctuation and special characters
# 3. Remove emojis
# 4. Expand slang and short forms (u -> you)
# 5. Correct spelling mistakes
# 6. Normalize repeated characters (sooo -> so)
# 7. Tokenization (split into words)
# 8. Remove stopwords (like "is", "the", "and")

# Conclusion:
# Cleaning and preprocessing messy text is essential in NLP tasks
# as it improves model accuracy and ensures better understanding of text data.