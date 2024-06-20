import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 球の表面をプロット
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 球の表面のデータを生成
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# 半透明の球体をプロット
ax.plot_surface(x, y, z, color='#ffecec', alpha=0.5, rstride=4, cstride=4)

# φとθの範囲を設定
phi = np.linspace(0, 2 * np.pi, 500)
theta = np.linspace(0, 2 * np.pi, 500)

# パラメトリック曲線のデータを生成
x_curve = np.cos(phi) * np.sin(theta)
y_curve = np.sin(phi) * np.sin(theta)
z_curve = np.cos(theta)

# パラメトリック曲線をプロット
ax.plot(x_curve, y_curve, z_curve, color='r', lw=2)

# プロットのラベルを設定
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3D Parametric Curve on a Sphere')
# ax.set_facecolor((1, 1, 1, 0))  # 背景を透明に設定
ax.axis("off")
plt.show()

