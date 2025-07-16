# Write a python function to remove a given word from a list and strip it at the same
# time.

# Ek function bana rahe hain jiska naam 'rem' hai
# Ye function 2 cheeze lega: ek list 'l' aur ek word 'word' jise hatana hai
def rem(l, word):
    n = []  # Ek khaali list banayi jisme hum cleaned items daalenge

    # Har item ke liye list 'l' me loop chalayenge
    for item in l:

        # Agar item exactly 'word' ke barabar nahi hai (jaise "an"), to hi aage badhenge
        if not (item == word):

            # item.strip(word):
            # Ye item ke start aur end se 'word' ke characters hata dega (not full word)
            # Jaise "Rohan" => "Roh" (kyunki end me 'n' tha)
            # "Shubham" => same rahega
            # "an" => skip ho gaya kyunki condition fail thi
            n.append(item.strip(word))

    return n  # Final cleaned list return kar rahe hain

# Original list jisme kuch words hain
l = ["Harry", "Rohan", "Shubham", "an"]

# Function ko call karke result print kar rahe hain
print(rem(l, "an"))

