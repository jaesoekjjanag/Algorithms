class SinglyLinkedListNode {
  constructor(nodeData) {
    this.data = nodeData;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  insertNode(nodeData) {
    const node = new SinglyLinkedListNode(nodeData);

    if (this.head == null) {
      this.head = node;
    } else {
      this.tail.next = node;
    }

    this.tail = node;
  }
}

const node1 = new SinglyLinkedListNode(1);
const node2 = new SinglyLinkedListNode(2);
const node3 = new SinglyLinkedListNode(3);

node1.next = node2;
node2.next = node3;
node3.next = node1;

function hasCycle1(head) {
  if (!head) return 0;

  const set = new Set();
  let cur = head;
  while (cur) {
    if (set.has(cur)) return 1;

    set.add(cur);
    cur = cur.next;
  }
}

function hasCycle2(head) {
  if (!head) return 0;

  let fast = head;
  let slow = head;

  while (fast) {
    fast = fast.next;
    if (fast) {
      fast = fast.next;
      slow = slow.next;
    }

    if (fast == slow) return 1;
  }

  return 0;
}

console.log(hasCycle1(node1));
console.log(hasCycle2(node1));
