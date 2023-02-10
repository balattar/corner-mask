import cv2
from pathlib import Path

def read(path: Path) -> None:
    path = path.expanduser() 
    mat: cv2.Mat = cv2.imread(filename=str(path.expanduser()))
    height, width, _ = mat.shape
    mask_color: list[int] = mat[0,0]
    print(mat.shape)
    height_scale: float = 0.7
    width_scale: float = 0.2
    for w in  range(0,int(width_scale*width)):
        for h in range(int(height_scale*height),int(height)):
            mat[h,w] = mask_color

    cv2.imshow(mat=mat,winname=str(path.expanduser()))
    cv2.waitKey(0)




if __name__ == "__main__":
    read(Path("~/Desktop/anvil-1.png"))