import glassdoor_scrapper as gs
import pandas as pd

path = "D:/My work world/Salary Prediction Model/chromedriver"

df = gs.get_jobs("data scientist", 10, False, path, 15)
