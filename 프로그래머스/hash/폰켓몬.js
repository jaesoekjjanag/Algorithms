function solution(nums) {
  const s = new Set(nums);
  const vary = Array.from(s).length;
  const half = nums.length / 2;

  return vary > half ? half : vary;
}
