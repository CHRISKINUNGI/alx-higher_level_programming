#!/usr/bin/node
exports.esrever = function (list) {
  const numberOfElements = list.length;
  const newList = [];
  for (let i = numberOfElements - 1; i !== -1; i--) {
    newList.push(list[i]);
  }
  return newList;
};
