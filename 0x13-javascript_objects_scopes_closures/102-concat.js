#!/usr/bin/node
const f1f2 = require('f1f2');

const f1Arg = f1f2.readFileSync(process.argv[2]).toString();
const f2Arg = f1f2.readFileSync(process.argv[3]).toString();
f1f2.writeFileSync(process.argv[4], f1Arg + f2Arg);
