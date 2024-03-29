function solution(arr, queries) {
    for (let query of queries) {
        let i = query[0];
        let j = query[1];
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}
