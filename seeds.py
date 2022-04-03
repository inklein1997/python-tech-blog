from app.models import Users, Posts, Comments
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  Users(user='alesmonde0', password='password123'),
  Users(user='jwilloughway1', password='password123'),
  Users(user='iboddam2', password='password123'),
  Users(user='dstanmer3', password='password123'),
  Users(user='djiri4', password='password123')
])

db.commit()


db.add_all([
  Posts(title='Python/Flask', description="I just started to learn Python and flask simultaneously", user_id=1),
  Posts(title='Django', description="Django really does have everything you need to build an app quickly!", user_id=2),
  Posts(title='Express', description="I learned to build back-ends using JavaScript and express", user_id=3),
  Posts(title='My least favorite thing about JavaScript', description="I am building a back-end CMS style command-line application, and I found myself in callback hell.  I spent hours trying to resolve this issue!", user_id=4),
  Posts(title='LinkedIn tips?', description="Does anyone have any good LinkedIn tips?  I am trying to land a job right now!", user_id=5)
])

db.commit()

db.add_all([
  Comments(content='That is awesome!  Python is a pretty straight forward language with syntax that is not too complex.  You will get it down in no time at all!', user_id=2, post_id=1),
  Comments(content='Thanks, @jwilloughway1!  Yeah I graduated from a full stack web development bootcamp on 3/18/22.  I have bee napplying for jobs, but alot of job descriptions require that you have python experience.  So I am trying to expand my skillset!', user_id=1, post_id=1),
  Comments(content='Yessir! It definitely does!  It is known to be like flask but has "batteries included".', user_id=5, post_id=2),
  Comments(content='What kind of npm packages do you use with express?', user_id=2, post_id=3),
  Comments(content='I use express session and apollo client server!', user_id=3, post_id=3),
  Comments(content='UGH... yes... I too know the struggle of callback hell. *sighs audibly*',user_id=1, post_id=4),
  Comments(content='Have you set your status to "looking for work"?  That will help employers see you!', user_id=4, post_id=5),
  Comments(content='That is very helpful!  Thank you!', user_id=5, post_id=5)
])

db.commit()

db.close()