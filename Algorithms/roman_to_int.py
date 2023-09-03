class Solution:
    roman_to_int_mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    def romanToInt(self, s: str) -> int:
        previous_item = None
        list_of_int_items = []
        list_of_roman_items = list(s)

        for roman_item in list_of_roman_items:
            int_from_mapping = self.roman_to_int_mapping[roman_item]
            if (roman_item == "V" or roman_item == "X") and previous_item == "I":
               list_of_int_items.pop()
               list_of_int_items.append(int_from_mapping - 1)
               print(f"For roman item {roman_item} add integer {int_from_mapping - 1}")
            elif (roman_item == "L" or roman_item == "C") and previous_item == "X":
                list_of_int_items.pop()
                list_of_int_items.append(int_from_mapping - 10)
                print(f"For roman item {roman_item} add integer {int_from_mapping - 10}")
            elif (roman_item == "D" or roman_item == "M") and previous_item == "C":
                list_of_int_items.pop()
                list_of_int_items.append(int_from_mapping - 100)
                print(f"For roman item {roman_item} add integer {int_from_mapping - 100}")
            else:
                list_of_int_items.append(int_from_mapping)
                print(f"For roman item {roman_item} add integer {int_from_mapping}")
            previous_item = roman_item
        return sum(list_of_int_items)

sol_cls = Solution()
#print(sol_cls.romanToInt("III"))
#print(sol_cls.romanToInt("MCMXCIV"))
print(sol_cls.romanToInt("IX"))