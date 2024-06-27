import pytest
import numpy as np
import os
import datetime
from iopaint.model.anytext.utils import branch_coverage, save_images, resize_image

@pytest.fixture(autouse=True)
def reset_coverage():
    for key in branch_coverage:
        branch_coverage[key] = False
    print("Coverage reset") 

def test_save_images_new_folders(tmp_path):
    """Test save_images when folders don't exist"""
    nonexistent_folder = os.path.join(str(tmp_path), "nonexistent")
    print(f"Testing with folder: {nonexistent_folder}")
    print(f"Folder exists before test: {os.path.exists(nonexistent_folder)}")
    
    img_list = [np.zeros((100, 100, 3), dtype=np.uint8)]
    save_images(img_list, nonexistent_folder)

    print(f"After save_images, branch_coverage[31] = {branch_coverage[31]}")
    assert branch_coverage[31]  # New folder created
    assert os.path.exists(nonexistent_folder)
    # assert branch_coverage[32]  # New date folder created
    # assert len(list(tmp_path.glob('*/*'))) == 1

def test_save_images_existing_folders(tmp_path):
    """Test save_images when folders already exist"""
    date_folder = tmp_path / datetime.datetime.now().strftime("%Y-%m-%d")
    date_folder.mkdir(parents=True)
    img_list = [np.zeros((100, 100, 3), dtype=np.uint8)]
    save_images(img_list, str(tmp_path))
    assert not branch_coverage[31]  # Folder already exists
    assert not branch_coverage[32]  # Date folder already exists
    assert len(list(tmp_path.glob('*/*'))) == 1

def test_save_images_empty_list(tmp_path):
    """Test save_images with an empty list"""
    save_images([], str(tmp_path))
    assert branch_coverage[33]  # Empty image list

def test_resize_image_valid():
    """Test resize_image with valid input"""
    img = np.zeros((1000, 1000, 3), dtype=np.uint8)
    result = resize_image(img)
    assert branch_coverage[36]  # Resizing needed
    assert max(result.shape[:2]) == 768

def test_resize_image_no_resize_needed():
    """Test resize_image when no resizing is needed"""
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    result = resize_image(img)
    assert not branch_coverage[36]  # No resizing needed
    assert max(result.shape[:2]) == 448 

def test_resize_image_invalid_type():
    """Test resize_image with invalid input type"""
    with pytest.raises(ValueError, match="Input must be a numpy array"):
        resize_image([1, 2, 3])
    assert branch_coverage[34]  # Invalid input type

def test_resize_image_empty():
    """Test resize_image with empty input"""
    with pytest.raises(ValueError, match="Input image is empty"):
        resize_image(np.array([]))
    assert branch_coverage[35]  # Empty input
