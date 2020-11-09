/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */

let heights = [1, 2];
let bricks = 0;
let ladders = 0;

let idx = 0;

var furthestBuilding = function (heights, bricks, ladders) {
  find(heights, bricks, ladders, 0);
  return idx;
};

console.log(furthestBuilding(heights, bricks, ladders));

function find(heights, leftBricks, leftLadders, curIdx) {
  let diff = heights[curIdx + 1] - heights[curIdx];
  // 더이상 갈 수 없음
  if (leftBricks < diff && leftLadders === 0) {
    if (curIdx > idx) {
      idx = curIdx;
    }
    return;
  } else if (curIdx >= heights.length - 1) {
    idx = curIdx;
    return;
  } else {
    // 다음 건물이 낮거나 같은 경우
    if (diff <= 0) {
      find(heights, leftBricks, leftLadders, curIdx + 1);
    } else {
      // 다음 건물이 더 높은 경우

      if (diff <= leftBricks) {
        find(heights, leftBricks - diff, leftLadders, curIdx + 1);
      }
      if (leftLadders >= 1) {
        find(heights, leftBricks, leftLadders - 1, curIdx + 1);
      }
    }
  }
}
