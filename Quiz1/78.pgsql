-- SELECT
--   name
-- FROM
--   referees;
-- SELECT
--   fourth_referee
-- FROM
--   match_referees
-- WHERE
--   match_num = 'M0003';
SELECT
  name
FROM
  referees
WHERE
  referee_id IN (
    SELECT
      fourth_referee
    FROM
      match_referees
    WHERE
      match_num = 'M0003'
  );