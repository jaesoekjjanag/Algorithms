const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

const node1 = new Node(1, null);

rl.on("line", (input) => {
  let [n, k] = input.split(" ");
  let root = node1;
  let node = node1;

  for (let i of Array(+n - 1).keys()) {
    newNode = new Node(i + 2);
    node.next = newNode;
    node = newNode;
  }
  node.next = root;

  let counter = 1;
  let last = root;
  const done = [];
  while (done.length < n) {
    if (!(counter % +k)) {
      done.push(root.value);
      next = root.next;
      last.next = next;
    }
    last = root;
    root = root.next;
    counter++;
  }

  console.log("<" + done.join(", ") + ">");
  rl.close();
});

//cd etc/linkedlist && node 오세푸스순열
