function solution(genres, plays) {
  const genreMap = genres.reduce((obj, g, i) => {
    const genre = obj[g];
    if (!genre) {
      obj[g] = [];
      obj[g][0] = plays[i];
      obj[g][1] = [i];
    } else {
      genre[0] += plays[i];
      genre[1] = [...genre[1], i].sort((a, b) => {
        const diff = plays[b] - plays[a];
        if (!diff) {
          return a - b;
        }

        return diff;
      });
    }
    return obj;
  }, {});

  return Object.values(genreMap)
    .sort((a, b) => b[0] - a[0])
    .reduce((prev, cur) => {
      return [...prev, ...cur[1].slice(0, 2)];
    }, []);
}
