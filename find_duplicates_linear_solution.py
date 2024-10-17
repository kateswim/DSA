def hasDuplicateValue(array):
    record_bank = {}
    for i in array:
        if i in record_bank:
            print("duplicate exists!", i)
            return True
        else:
            record_bank[i]=1
    print("no duplicate exists in this case", array)


hasDuplicateValue([1,2,3,4,5,1])
hasDuplicateValue([1,2,3,4,5])