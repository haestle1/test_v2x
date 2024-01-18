from test_v2x.data_utils.datasets.intermediate_fusion_dataset import IntermediateFusionDataset

__all__ = {
    'IntermediateFusionDataset': IntermediateFusionDataset
}

# the final range for evaluation
GT_RANGE = [-140, -40, -3, 140, 40, 1]
# The communication range for cavs
COM_RANGE = 70


def build_dataset(dataset_cfg, visualize=False, train=True):
    # dataset 구성을 포함하는 설정값을 기반으로 dataset 구성
    # late, early, intermediate으로 나눠진 dataset 중 하나를 선택하여 이를 기반으로 set 구성
    dataset_name = dataset_cfg['fusion']['core_method']
    error_message = f"{dataset_name} is not found. " \
                    f"Please add your processor file's name in opencood/" \
                    f"data_utils/datasets/init.py"
    assert dataset_name in ['IntermediateFusionDataset'], error_message

    dataset = __all__[dataset_name](
        params=dataset_cfg,
        visualize=visualize,
        train=train
    )

    return dataset
