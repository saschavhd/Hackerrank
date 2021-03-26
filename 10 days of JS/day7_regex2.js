function regexVar() {
    // const re = /^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]/g
    const re = /^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)([a-z]|[A-Z]){1,100}$/
    return re;
}
