SELECT
  name
FROM
  referees
WHERE
  referee_id IN (
    SELECT DISTINCT
      referee
    FROM
      match_referees
  )