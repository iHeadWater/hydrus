from usgs import api
# 首先在usgs eros上注册自己的账号，然后pip安装usgs，接着使用usgs的CLI工具登陆的账号。
# $ pip install usgs
# $ usgs login [USGS username] [USGS password]
# Set the EarthExplorer catalog
node = 'EE'

# Set the Hyperion dataset
hyperion_dataset = 'EO1_HYP_PUB'


# Set the scene ids
hyperion_scene_id = 'EO1H1820422014302110K2_SG1_01'


# Submit requests to USGS servers
api.metadata(hyperion_dataset, node, [hyperion_scene_id])
