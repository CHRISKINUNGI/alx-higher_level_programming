#!/usr/bin/node
function nbOccurences (list, searchElement) {
  return list.filter(element => element === searchElement).length;
}
module.exports = nbOccurences;
