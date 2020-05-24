data = get_pushshift_data(data_type="comment", q=TERM_OF_INTEREST, after=TIMEFRAME, size=1000, aggs="subreddit").get("aggs").get("subreddit")

df = pd.DataFrame.from_records(data)[0:10]

px.bar(df,
       x="key",
       y="doc_count",
       title=f"Subreddits with most activity - comments with '{TERM_OF_INTEREST}' in the last {TIMEFRAME}",
       labels={"doc_count": "# comments","key": "Subreddits"},
       color_discrete_sequence=[COMMENT_COLOR],
       height=500,
       width=800)
