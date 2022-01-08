function solution(arr){
  let max =0;
  arr.sort((a, b)=>a[1] - b[1]);
  for(let j =0; j< arr.length; j++){
    let temp =0;
    for(let i =0; i< arr.length; i++){
      if(arr[j][1] > arr[i][0] && arr[j][0] < arr[i][1] ){ 
        if(arr[j] != arr[i])
          temp ++
    }
    if(max < temp) max = temp;
    }
  }
console.log(max);
}

let arr1=[[14, 18], [12, 15], [15, 20], [20, 30], [5, 14]];
let arr2=[[1, 3], [4, 8], [5, 9], [6, 10]];
let arr3=[[1, 10], [2, 8], [3, 9]];

solution(arr1)
solution(arr2)
solution(arr3)