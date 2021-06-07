function sides(literals, ...expressions) {
    let s = [];
    s[1] = (expressions[1] + Math.sqrt(Math.pow(expressions[1], 2)-(16*expressions[0])))/4;
    s[0] = (expressions[1] - Math.sqrt(Math.pow(expressions[1], 2)-(16*expressions[0])))/4;
    return s;
}
