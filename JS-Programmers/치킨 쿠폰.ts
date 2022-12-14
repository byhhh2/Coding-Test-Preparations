function solution(chicken: number) {
  let serviceChicken = 0;
  let coupon = chicken;

  while (coupon >= 10) {
    serviceChicken += Math.floor(coupon / 10);
    coupon = Math.floor(coupon / 10) + (coupon % 10);
  }

  return serviceChicken;
}

console.log(solution(100));
