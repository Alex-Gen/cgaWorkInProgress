


            xhttp=new XMLHttpRequest();
            xhttp.open("GET","../XML/commenti.xml",false);
            xhttp.send();
            var xmlCommenti=xhttp.responseXML; // file commenti.xml

            console.log(document);
            console.log(xmlCommenti);
                
            window.onload = function () {
                
                var n = 2; // numero post home, modificare all'aggiunta di nuovi post(!)

                for (var j = 1; j<=n ; j++){

                    var boxPost = document.getElementById('post'+j);
                    var boxCommenti = boxPost.getElementsByClassName("commentiInseriti");

                    var commenti=xmlCommenti.getElementsByTagName("commento");  
                    //var output='';
                    var contenitore = document.createElement("div");

                    for (var i = 0; i < commenti.length; i++) {
                        var commento = commenti[i];
                        if (commento.getElementsByTagName("post")[0].textContent=='post'+j) { // commenti correlati al post
                            var user = commento.getElementsByTagName("user")[0].textContent;
                            var post = commento.getElementsByTagName("post")[0].textContent;
                            var data = commento.getElementsByTagName("data")[0].textContent;
                            var contenuto = commento.getElementsByTagName("contenuto")[0].textContent;
                            //output += '<div class="commento"><p>'+contenuto+'</p><span>aggiunto da '+user+' il:'+data+'</span></div>';

                            var div = document.createElement("div");
                            div.classList.add("commento");
                            
                            var p = document.createElement("p");
                            var txt = document.createTextNode(contenuto);
                            p.appendChild(txt);

                            var span = document.createElement("span");

                            div.appendChild(p);
                            div.appendChild(span);

                            txt = document.createTextNode("aggiunto da: "+user+" "+data);
                            span.appendChild(txt);    

                            contenitore.appendChild(div);   

                        }
                    } // fine ciclo

                    // scrivo nella pagina l'output
                    //var txt = document.createTextNode(output);
                    //boxCommenti.innerText = output;
                    boxCommenti[0].appendChild(contenitore);
                    console.log(boxCommenti[0]);
                    //console.log(boxCommenti.innerText);


                } // fine for
            }
            