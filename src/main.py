from flet import app, AppView
from launcher import Launcher

app(target=Launcher, view=AppView.FLET_APP, assets_dir="assets", name="Onelauncher")