#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log("Missing size");
} else {
	const n = Number(process.argv[2]);
	for (let c = 0; c < n; c++) {
		console.log("X".repeat(n));
	}
}
