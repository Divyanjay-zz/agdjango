    (function(){
            $(document).ready(function(){
                var gridDiv = document.querySelector('#myGrid');
            var selectedCount= "";
             var gridOptions = {

                    columnDefs: [
                        {headerName: 'date_time', field: 'date_time'},
                        {headerName: 'id', field: 'id',valueGetter: function(params){
                            if (selectedCount =="id"){
                                return params.data.id;
                            }
                            else {

                            return params.data.cg_fees;
                        }}
                        }                       
                    ]
                };
                new agGrid.Grid(gridDiv, gridOptions);
               
                var getData = $.ajax('/aggrid/agdu/');                  
                
                getData.then(function(response, statusText, xhrObj){
                    
                    console.log(xhrObj);
                    
                    gridOptions.api.setRowData(response.data);
                }, 
                function(xhrObj, textStatus, err){
                    console.log(err);
                })
               document.querySelector('#id').addEventListener('click',function(){
                selectedCount = "id";
                gridOptions.api.refreshView();
               });
               document.querySelector('#cg_fees').addEventListener('click',function(){
               selectedCount = "cg_fees";
                gridOptions.api.refreshView();
               });
 
            })            
        })(); 