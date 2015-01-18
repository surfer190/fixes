#CGridView, CButtonColumn and CSqlDataProvider Trying to set property of Undefined Error

The error arises because the $data attribute is reference like this $data['id'] instead of $data->id in the CSqlDataProvider

So to Fix this Error you must Override the default settings of the following

```
'viewButtonUrl'=>'Yii::app()->controller->createUrl("/share/draw",array("id"=>$data["id"]))',
      		'updateButtonUrl'=>'Yii::app()->controller->createUrl("/ajax/updateWatchlist",array("id"=>$data["id"]))',
			      		'deleteButtonUrl'=>'Yii::app()->controller->createUrl("/ajax/deleteWatchlist",array("id"=>$data["id"]))',
						```
