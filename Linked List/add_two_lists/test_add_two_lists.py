import unittest
from add_two_list import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def testAddTwoNumbers(self):
        
        lis1 = [1, 2, 3]
        lis2 = [2, 5, 8]
        head1 = ListNode(lis1[0])
        l_lis1 = head1
        for i in range(1, len(lis1)):
            l_lis1.next = ListNode(lis1[i])
            l_lis1 = l_lis1.next

        head2 = ListNode(lis2[0])
        l_lis2 = head2
        for i in range(1, len(lis2)):
            l_lis2.next = ListNode(lis2[i])
            l_lis2 = l_lis2.next
        

        result = Solution.addTwoNumbers(self, head1, head2)
        self.assertEqual(result.val ,3 )

if __name__ == '__main__':
    unittest.main()