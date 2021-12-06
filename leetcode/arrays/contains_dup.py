def containsDuplicate(self, nums: List[int]) -> bool:
    hash = set()
    for element in nums:
        if element in hash:
            return True
        hash.add(element)
    return False
