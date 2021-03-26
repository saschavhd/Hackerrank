function getCount(objects) {
    let res = 0;
    for (let i = 0; i < objects.length; i++) {
        if (objects[i].x == objects[i].y) {
            res++
        }
    }
    return res
}
