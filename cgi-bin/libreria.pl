
#====================================================================================
# Funzione &leggiPost()
#
# Legge lo standard input (in questo caso metodo POST di una for)
# e restituisce un hash contenente i dati.
#
sub leggi_post()
{	
	my($buffer, $nome, $valore, @pairs, %DATI);
	
	read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    #
    # Suddivide la richiesta in un array di coppie «nome=valore».
    #
    @pairs = split (/&/, $buffer);
    #
    # Elabora ogni coppia contenuta nell'array.
    #
    foreach my $elemento (@pairs)
      {
        #
        # Scompone la coppia.
        #
        ($nome, $valore) = split ('=', $elemento);
        #
        # Trasforma «+» in spazio.
        #
        $valore =~ tr/+/ /;
        $nome =~ tr/+/ /;
        #
        # Trasforma «%hh» nel carattere corrispondente.
        #
        $nome   =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        $valore =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        #
        # Aggiunge la coppia decodificata in un hash.
        #
        $DATI{$nome} = $valore;
      }
      # Restituisce l'hash delle coppie ( nome => valore )
      return (%DATI);
}
#====================================================================================
# dato che è una libreria deve ritornare un valore di tipo true
1;
