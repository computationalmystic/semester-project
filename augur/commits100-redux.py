    @annotate(tag='commits100')
    def commits100(self, owner, repo=None):
        """
        Timeseries of the count of commits, limited to the first 100 overall

        :param owner: The name of the project owner or the id of the project in the projects table of the project in the projects table. Use repoid() to get this.
        :param repo: The name of the repo. Unneeded if repository id was passed as owner.
        :return: DataFrame with commits/day
        """
        repoid = self.repoid(owner, repo)
        commitsSQL = s.sql.text("""
            SELECT COUNT(*) AS 'commits_count'
            FROM commits
            WHERE commits.project_id = :repoid
            AND
            created_at > (CURRENT_DATE-220) 
        """)
        #return pd.read_sql(rawContributionsSQL, self.db, params={"repoid": str(repoid)})

        temp = pd.read_sql(commitsSQL, self.db, params={"repoid": str(repoid)})
        tem = temp['commits_count'] > 0
        #return temp[tem].reset_index(drop=True)
        return tem